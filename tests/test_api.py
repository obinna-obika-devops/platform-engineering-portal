from fastapi.testclient import TestClient
from portal.api import app
c=TestClient(app)
def test_dev_plan():
    r=c.post('/provision/plan',json={'name':'orders','runtime':'python','environment':'dev'})
    assert r.status_code==200 and 'repository' in r.json()['artifacts']
def test_prod_requires_approval():
    r=c.post('/provision/plan',json={'name':'orders','runtime':'go','environment':'prod'})
    assert r.json()['approval_required'] is True
