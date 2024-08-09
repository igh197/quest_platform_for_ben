# quest_platform_for_ben

This project is developed by 3 FastAPI Server in MSA.

1. Users Server
   1. This server controls user management. So it is charged to log in, sign up, user authentication
2. QuestCatalog Server
   1. This server controls crud of Reward and Quest table.  
3. QuestProcess Server
   1. This server controls quest's business logic. So it is the main feature server.


I used docker & docker-compose to control the container server.

I used AWS RDS MySQL for each databases.

There are my Dockerfiles and docker-compose.yml in gitHub.

## API Documentation


### **Quest API**


#### **1. Create Quest**

- **Endpoint**: `POST /quest/create/{reward_id}`
- **Description**: Creates a quest associated with the given reward ID.
- **Request Parameters**:
  - `reward_id` (path parameter, int): The ID of the reward to be linked with the quest.
  - **Body**: `QuestCreate` (JSON object)
    - `name`: Name of the quest (string)
    - `description`: Description of the quest (string)
- **Response**:
  - **Status Code**: 201 Created
  - **Body**: `QuestCreate` object
    - `id`: ID of the created quest (int)
    - `name`: Name of the quest (string)
    - `description`: Description of the quest (string)

---

#### **2. Get Quest**

- **Endpoint**: `GET /quest/{quest_id}`
- **Description**: Retrieves a quest by its ID.
- **Request Parameters**:
  - `quest_id` (path parameter, int): The ID of the quest to retrieve.
- **Response**:
  - **Status Code**: 200 OK
  - **Body**: `QuestRead` object
    - `id`: ID of the quest (int)
    - `name`: Name of the quest (string)
    - `description`: Description of the quest (string)

---

#### **3. Update Quest**

- **Endpoint**: `PUT /quest/update/{quest_id}`
- **Description**: Updates a quest by its ID.
- **Request Parameters**:
  - `quest_id` (path parameter, int): The ID of the quest to update.
  - **Body**: `QuestCreate` (JSON object)
    - `name`: Name of the quest (string)
    - `description`: Description of the quest (string)
- **Response**:
  - **Status Code**: 200 OK
  - **Body**: `QuestCreate` object (updated content)
  - **Error Response**:
    - **Status Code**: 404 Not Found
    - **Body**: `{"detail": "Quest not found"}`

### **Reward API**

---

#### **4. Create Reward**

- **Endpoint**: `POST /reward/create`
- **Description**: Creates a new reward.
- **Request Parameters**:
  - **Body**: `RewardCreate` (JSON object)
    - `name`: Name of the reward (string)
    - `points`: Points associated with the reward (int)
- **Response**:
  - **Status Code**: 201 Created
  - **Body**: `RewardCreate` object
    - `id`: ID of the created reward (int)
    - `name`: Name of the reward (string)
    - `points`: Points associated with the reward (int)

---

#### **5. Get Reward**

- **Endpoint**: `GET /reward/{reward_id}`
- **Description**: Retrieves a reward by its ID.
- **Request Parameters**:
  - `reward_id` (path parameter, int): The ID of the reward to retrieve.
- **Response**:
  - **Status Code**: 200 OK
  - **Body**: `RewardRead` object
    - `id`: ID of the reward (int)
    - `name`: Name of the reward (string)
    - `points`: Points associated with the reward (int)

---

#### **6. Update Reward**

- **Endpoint**: `PUT /reward/update/{reward_id}`
- **Description**: Updates a reward by its ID.
- **Request Parameters**:
  - `reward_id` (path parameter, int): The ID of the reward to update.
  - **Body**: `RewardCreate` (JSON object)
    - `name`: Name of the reward (string)
    - `points`: Points associated with the reward (int)
- **Response**:
  - **Status Code**: 200 OK
  - **Body**: `RewardCreate` object (updated content)
  - **Error Response**:
    - **Status Code**: 404 Not Found
    - **Body**: `{"detail": "Reward not found"}`

---



### **Authentication and User Management API**

---

#### **1. User Signup**

- **Endpoint**: `POST /signup`
- **Description**: Creates a new user with a hashed password and default values for `gold`, `diamond`, and `status`.
- **Request Body**:
  - **`UserCreate` (JSON object)**:
    - `user_name`: Username of the new user (string, required)
    - `password`: Password for the new user (string, required)
- **Response**:
  - **Status Code**: 201 Created
  - **Body**: `UserRead` object
    - `user_id`: ID of the created user (int)
    - `user_name`: Username of the created user (string)
    - `gold`: Initial gold amount (int, default is 20)
    - `diamond`: Initial diamond amount (int, default is 0)
    - `status`: Status of the user (int, default is 0)
- **Error Response**:
  - **Status Code**: 409 Conflict
  - **Body**: `{"detail": "User already exists"}`

---

#### **2. Get User Information**

- **Endpoint**: `GET /user/{user_id}`
- **Description**: Retrieves user information by user ID.
- **Request Parameters**:
  - `user_id` (path parameter, int): The ID of the user to retrieve.
- **Response**:
  - **Status Code**: 200 OK
  - **Body**: User information (e.g., `UserRead` object with `user_id`, `user_name`, etc.)

---

#### **3. Update User Information**

- **Endpoint**: `PUT /user/{user_id}`
- **Description**: Updates user information for the specified user ID.
- **Request Parameters**:
  - `user_id` (path parameter, int): The ID of the user to update.
  - **Body**: `UserCreate` (JSON object)
    - `user_name`: Updated username (string, optional)
    - `password`: Updated password (string, optional)
- **Response**:
  - **Status Code**: 200 OK
  - **Body**: Updated user information (e.g., `UserRead` object)
  - **Error Response**:
    - **Status Code**: 404 Not Found
    - **Body**: `{"detail": "User not found"}`

---

#### **4. User Login**

- **Endpoint**: `POST /login`
- **Description**: Authenticates a user and returns an access token.
- **Request Body**:
  - **`UserLogin` (JSON object)**:
    - `user_name`: Username of the user (string, required)
    - `password`: Password of the user (string, required)
- **Response**:
  - **Status Code**: 200 OK
  - **Body**: `{"access_token": "JWT_ACCESS_TOKEN"}`
- **Error Responses**:
  - **Status Code**: 401 Unauthorized
    - **Body**: `{"detail": "Invalid username or password"}`
  - **Status Code**: 401 Unauthorized
    - **Body**: `{"detail": "You are banned"}`

---

#### **5. Access Protected Resource**

- **Endpoint**: `GET /protected`
- **Description**: Retrieves the currently authenticated user's information using JWT.
- **Request Headers**:
  - **Authorization**: `Bearer JWT_ACCESS_TOKEN`
- **Response**:
  - **Status Code**: 200 OK
  - **Body**: `UserRead` object
- **Error Responses**:
  - **Status Code**: 404 Not Found
    - **Body**: `{"detail": "User not found"}`

---

### **Notes**

- **JWT Configuration**: The JWT configuration is loaded using the `@AuthJWT.load_config` decorator, and it uses the secret key defined in the application settings (`settings.JWT_SECRET_KEY`).
- **Password Hashing**: Passwords are hashed using `bcrypt` for secure storage.
- **Third-Party Service Interaction**: The login endpoint interacts with an external quest checker service based on the number of login attempts.

### **How to Run**

- The application can be run using Uvicorn:
  ```bash
  uvicorn run(app, reload=True)
  


### **Quest and Reward API**

---

#### **1. Create User Quest Reward**

- **Endpoint**: `POST /quest_checker/{user_id}/{quest_id}`
- **Description**: Creates a record of a user's quest reward. Associates a quest with a user and records the claim status and date.
- **Request Parameters**:
  - `user_id` (path parameter, int): The ID of the user who is claiming the quest reward.
  - `quest_id` (path parameter, int): The ID of the quest being claimed.
  - **Body**: `claim` (string): The status of the claim (e.g., 'claimed', 'not claimed').
- **Request Body**:
  - **`UserQuestRewardBase` (JSON object)**:
    - `user_id`: The ID of the user (int, required)
    - `status`: The status of the claim (string, required)
    - `date`: The date of the claim (date, automatically set to the current date)
- **Response**:
  - **Status Code**: 201 Created
  - **Body**: `UserQuestRewardBase` object
    - `user_id`: The ID of the user (int)
    - `status`: The status of the claim (string)
    - `date`: The date of the claim (date)

- ### **Notes**

- **Date Handling**: The `date` field is automatically set to the current date when creating the record.
- **Database Interaction**: Uses SQLAlchemy for database interactions.

### **How to Run**

- The application can be run using Uvicorn:
  ```bash
  uvicorn run(app, reload=True)




