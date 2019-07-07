mkdir upload_pic\n
cd upload_pic
git clone git@github.com:johnson329/upload_pic_project.git
pip3 install virtualenv
virtualenv --no-site-packages venv
source venv/bin/activate
pip3 install -r requirements
python manage.py runserver