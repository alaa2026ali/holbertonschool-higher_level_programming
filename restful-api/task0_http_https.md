# Task 0: Basics of HTTP/HTTPS

## Difference Between HTTP and HTTPS

HTTP (HyperText Transfer Protocol) is the standard protocol used for communication between a client and a web server. It transfers data in plain text, making it vulnerable to interception by attackers.

HTTPS (HyperText Transfer Protocol Secure) is the secure version of HTTP. It uses SSL/TLS encryption to protect the data exchanged between the client and the server. This encryption ensures confidentiality, integrity, and authentication, making HTTPS suitable for websites that handle sensitive information such as passwords, payment details, and personal data.

### Key Differences

| HTTP                                      | HTTPS                                        |
| ----------------------------------------- | -------------------------------------------- |
| Data is not encrypted                     | Data is encrypted using SSL/TLS              |
| Uses port 80                              | Uses port 443                                |
| Less secure                               | More secure                                  |
| Vulnerable to eavesdropping and tampering | Protects against eavesdropping and tampering |
| Suitable for public information           | Suitable for sensitive information           |

---

## Structure of an HTTP Request

An HTTP request is sent from the client to the server and contains the following components:

* **Request Method:** Specifies the action to perform (GET, POST, PUT, DELETE, etc.).
* **URL/Path:** Identifies the requested resource.
* **HTTP Version:** Indicates the HTTP protocol version.
* **Headers:** Provide additional information about the request (Host, User-Agent, Content-Type, Authorization, etc.).
* **Body (Optional):** Contains data sent to the server, mainly used with POST and PUT requests.

### Example

```http
GET /users HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: application/json
```

---

## Structure of an HTTP Response

An HTTP response is sent from the server back to the client and contains:

* **HTTP Version**
* **Status Code** (e.g., 200, 404)
* **Status Message** (OK, Not Found, etc.)
* **Headers**
* **Response Body (Optional)**

### Example

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "message": "Success"
}
```

---

## Common HTTP Methods

| Method | Description                           | Use Case                                 |
| ------ | ------------------------------------- | ---------------------------------------- |
| GET    | Retrieves data from the server.       | Fetching a web page or data from an API. |
| POST   | Creates a new resource on the server. | Creating a new user account.             |
| PUT    | Updates an existing resource.         | Updating a user's profile information.   |
| DELETE | Removes a resource from the server.   | Deleting a user account.                 |

---

## Common HTTP Status Codes

| Status Code                   | Description                                 | Example Scenario                                      |
| ----------------------------- | ------------------------------------------- | ----------------------------------------------------- |
| **200 OK**                    | The request was successful.                 | Retrieving user information successfully.             |
| **201 Created**               | A new resource was created successfully.    | Creating a new user.                                  |
| **400 Bad Request**           | The request contains invalid data.          | Missing required fields in a form submission.         |
| **404 Not Found**             | The requested resource could not be found.  | Accessing a page or API endpoint that does not exist. |
| **500 Internal Server Error** | An unexpected error occurred on the server. | Database connection failure or application crash.     |

---

## HTTP Status Code Categories

* **1xx** – Informational responses.
* **2xx** – Successful responses.
* **3xx** – Redirection messages.
* **4xx** – Client errors.
* **5xx** – Server errors.

