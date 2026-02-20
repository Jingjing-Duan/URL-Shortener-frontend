# URL-Shortener-frontend

## Frontend Features

The frontend is responsible for user interaction and communication with the backend API.

### 1. URL Input Form
- Allows users to enter a long URL.
- Optional custom alias field.
- Basic client-side validation:
  - URL must start with `http://` or `https://`
  - Alias must match allowed format (A–Z, a–z, 0–9, `_`, `-`, 3–32 chars)

### 2. API Integration
- Sends `POST /api/shorten` requests to the backend.
- Displays returned `short_url`.
- Handles HTTP status codes (201, 200, 400, 409).
- Shows user-friendly error messages.

### 3. Short Link Display
- Displays generated short URL.
- Provides "Copy to Clipboard" functionality.
- Shows success feedback after copying.

### 4. Session History (In-Memory)
- Displays recently generated short links.
- Stored only in browser memory.
- Cleared when the page is refreshed.
- Keeps up to the latest 10 entries.

### 5. Loading & UX Handling
- Disables button during API call.
- Shows loading state ("Creating...").
- Prevents accidental multiple submissions.

### 6. Security (Frontend-Level)
- Basic input validation (UX-level only).
- User input is sanitized using `escapeHtml()` to prevent Cross-Site Scripting (XSS).

---

## Backend Integration (Final API Contract)

This frontend does not access the database. It communicates with the backend service via HTTP.

### Configuration
Set the backend base URL using an environment variable:

- `BACKEND_BASE_URL`  
  Example (local): `http://127.0.0.1:8001`  
  Example (Azure): `https://<backend-app>.azurewebsites.net`

The frontend calls:  
`POST ${BACKEND_BASE_URL}/api/shorten`

> Note: The backend must return an **absolute** `short_url` (including protocol + host), e.g. `https://<backend>/r/<code>`.

---

### 1) Create Short Link
**Endpoint:** `POST /api/shorten`  
**Content-Type:** `application/json`

**Request body:**
```json
{
  "url": "https://example.com/some/long/link",
  "custom_code": "optional-alias"
}
```
---

### 2) Response (201 Created / 200 OK)
```json
{
  "code": "Ab3Xk9",
  "short_url": "https://<backend-domain>/r/Ab3Xk9"
}
```

### 3) Error responses:  
#### 400 Bad Request
```json
{ "error": "Invalid URL" }
```
#### 409 Conflict
```json
{ "error": "custom_code taken" }
```

