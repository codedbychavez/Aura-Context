import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

clf_model_dir = os.path.join(base_dir, 'ai_core/clf')
clf_models_dir = os.path.join(base_dir, 'clf_models')
clf_model_root_intents_json_file = os.path.join(clf_model_dir, 'clf_models/root/root_intents.json')
root_clf_model_vectorizer = os.path.join(clf_model_dir, 'clf_models/root/vectorizer.pickle')
root_clf_model = os.path.join(clf_model_dir, 'clf_models/root/clf.model')

update_clf_model_dir = os.path.join(clf_model_dir, 'clf_models/update_intents')

svp_model_dir = os.path.join(base_dir, 'ai_core/svp/svp_models')
svp_model_dir_core = os.path.join(base_dir, 'ai_core/svp')
svp_model_json_file = os.path.join(svp_model_dir_core, 'json/ai_svps.json')

wipe_clf_model_path = os.path.join(clf_model_dir, 'clf_models')
wipe_svp_model_path = os.path.join(svp_model_dir_core, 'svp_models')