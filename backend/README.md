# Backend Notes API

Endpoints:
- GET /api/health/
- GET /api/notes/
- POST /api/notes/
- GET /api/notes/<id>/
- PUT /api/notes/<id>/
- PATCH /api/notes/<id>/
- DELETE /api/notes/<id>/

Run migrations:
- python manage.py migrate
- python manage.py loaddata (optional) or `python manage.py seed_notes`

CORS:
- CORS is configured to allow all origins for ease of local development. For production, restrict to the frontend origin (e.g., http://localhost:3000).
