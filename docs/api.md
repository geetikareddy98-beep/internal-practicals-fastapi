# Items API documentation

Run `python -m uvicorn app.main:app --reload` after installing dependencies. The default local base URL is `http://127.0.0.1:8000`.

## GET /health

Reports process responsiveness. No parameters or request body. Returns HTTP 200 and `{"status":"ok"}`. This does not check an external database or prove deployment readiness.

## POST /items

Send `Content-Type: application/json` and `{"name":"Notebook"}`. `name` is required, must be a string and must contain 1–100 characters. Success returns HTTP 201 with `{"name":"Notebook","id":1}`; JSON property order is immaterial. Identifiers increase within the current process. Repeated names are allowed.

Empty strings, missing names, null, numbers, booleans, arrays, objects and names longer than 100 characters return HTTP 422 with a `detail` list describing the location and validation failure. Malformed JSON also returns 422. Validation failures do not create records or consume identifiers. Whitespace is preserved and is not stripped.

## Generated documentation

- `/docs`: Swagger UI
- `/redoc`: ReDoc
- `/openapi.json`: machine-readable OpenAPI schema

The tests verify required fields, name lengths and documented 200/201/422 responses. The saved `docs/openapi.json` is generated from the application, not handwritten.

## Storage and configuration

No credentials or environment variables are required. The global in-memory list resets on restart and is unsuitable for concurrent production use or multiple worker processes. There is no update/delete API, persistence, pagination, rate limiting or authorization in this teaching contract. Add such behavior only under a separately defined requirement.
