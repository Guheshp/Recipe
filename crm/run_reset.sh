rm -f "db.backends.mysql"

#run the migrations 
python3 manage.py makemigrations
python3 manage.py migrate

#create superuser 
echo "from user.models import CustomerUser; CustomerUser.objects.create_superuser('gp', 'guheshpanjagll481@gmail.com', 'gp@123')" | python3 manage.py

#prepare dummy data 
python3 manage.py generate_dymmy_data