from models import FeatureRequest

def check_feature_req_with_same_priority_for_client(client_id, priority, db):
    result = db.session.query(FeatureRequest) \
        .filter(FeatureRequest.client == client_id, 
                FeatureRequest.client_priority == priority).all()
    return len(result) > 0

def update_all_feature_req_with_equal_greater_priority(client_id, priority, db):
    result = db.session.query(FeatureRequest) \
        .filter(FeatureRequest.client == client_id, 
                FeatureRequest.client_priority >= priority) \
        .order_by(FeatureRequest.client_priority).all()

    messages = []
    for r in result:
        r.client_priority = r.client_priority + 1
        messages.append("Feature request " + str(r.title) + " is updated with priority " + str(r.client_priority) + ".")
    
    return messages
    