
# API Documentation

This document provides details on the API routes used for managing game sessions. Each route corresponds to an operation related to game session creation, updating, and retrieval.

## Routes

### 1. **Create Session**
- **Endpoint:** `POST /api/sessions/`
- **Description:** Creates a new game session with a single player.
- **Request Body:**
  ```json
  {
    "player_name": "Player 1"
  }
  ```
  - `player_name` (string): The name of the player starting the session.
  
- **Response:**
  - **Status:** `201 Created`
  - **Body:**
  ```json
  {
    "session_name": "ABCDE",
    "player_one_name": "Player 1",
    "player_two_name": null,
    "player_one_score": 0,
    "player_two_score": 0,
    "turn": 0,
    "created_at": "2025-01-18T00:00:00Z"
  }
  ```

### 2. **Get Session**
- **Endpoint:** `GET /api/sessions/{session_name}/`
- **Description:** Retrieves information for a specific session by its name.
- **Path Parameters:**
  - `session_name` (string): The name of the session (5-character string).
  
- **Response:**
  - **Status:** `200 OK`
  - **Body:**
  ```json
  {
    "session_name": "ABCDE",
    "player_one_name": "Player 1",
    "player_two_name": null,
    "player_one_score": 0,
    "player_two_score": 0,
    "turn": 0,
    "created_at": "2025-01-18T00:00:00Z"
  }
  ```

### 3. **Join Session**
- **Endpoint:** `POST /api/sessions/{session_name}/join/`
- **Description:** Joins an existing session with the given name, adding the player if the session has space.
- **Path Parameters:**
  - `session_name` (string): The name of the session.
  
- **Request Body:**
  ```json
  {
    "player_name": "Player 2"
  }
  ```
  - `player_name` (string): The name of the player joining the session.

- **Response:**
  - **Status:** `200 OK` (If the player successfully joins the session)
  - **Body:**
  ```json
  {
    "session_name": "ABCDE",
    "player_one_name": "Player 1",
    "player_two_name": "Player 2",
    "player_one_score": 0,
    "player_two_score": 0,
    "turn": 1,
    "created_at": "2025-01-18T00:00:00Z"
  }
  ```
  
  - **Status:** `400 Bad Request` (If the session is already full)
  - **Body:**
  ```json
  {
    "error": "Session is already full"
  }
  ```

### 4. **Delete Session**
- **Endpoint:** `DELETE /api/sessions/{session_name}/`
- **Description:** Deletes an existing session by its name.
- **Path Parameters:**
  - `session_name` (string): The name of the session to delete.

- **Response:**
  - **Status:** `200 OK`
  - **Body:**
  ```json
  {
    "message": "Session ABCDE deleted successfully"
  }
  ```

### 5. **List Sessions**
- **Endpoint:** `GET /api/sessions/`
- **Description:** Lists all available game sessions.
  
- **Response:**
  - **Status:** `200 OK`
  - **Body:**
  ```json
  [
    {
      "session_name": "ABCDE",
      "player_one_name": "Player 1",
      "player_two_name": "Player 2",
      "player_one_score": 5,
      "player_two_score": 3,
      "turn": 2,
      "created_at": "2025-01-18T00:00:00Z"
    },
    {
      "session_name": "XYZ12",
      "player_one_name": "Alice",
      "player_two_name": null,
      "player_one_score": 0,
      "player_two_score": 0,
      "turn": 0,
      "created_at": "2025-01-18T00:00:00Z"
    }
  ]
  ```

### 6. **End Turn**
- **Endpoint:** `PATCH /api/sessions/{session_name}/end_turn/`
- **Description:** Updates the scores for each player and increments the turn counter for a specific session.
- **Path Parameters:**
  - `session_name` (string): The name of the session.

- **Request Body:**
  ```json
  {
    "player_one_points": 5,
    "player_two_points": 3
  }
  ```
  - `player_one_points` (integer): The points to be added to Player 1's score.
  - `player_two_points` (integer): The points to be added to Player 2's score.

- **Response:**
  - **Status:** `200 OK`
  - **Body:**
  ```json
  {
    "session_name": "ABCDE",
    "player_one_name": "Player 1",
    "player_two_name": "Player 2",
    "player_one_score": 5,
    "player_two_score": 3,
    "turn": 1,
    "created_at": "2025-01-18T00:00:00Z"
  }
  ```

---

## Error Codes

- **400 Bad Request:**
  - If a session is full when trying to join.
  - If the `player_name` is not provided when creating or joining a session.

- **404 Not Found:**
  - If the session with the given `session_name` does not exist (in `GET`, `DELETE`, or `PATCH` requests).

- **500 Internal Server Error:**
  - If there’s a problem with the server processing the request.

---

### Notes:

- Each session has a unique 5-character `session_name` generated upon creation.
- Player names and session data (scores, turns) are updated dynamically as users interact with the session.
- Player 1 starts the session, and Player 2 can join if the session isn't full.
