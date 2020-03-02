import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


project_id = 'hzhome'

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': project_id,
})

db = firestore.client()
