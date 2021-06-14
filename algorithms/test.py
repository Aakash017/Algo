l = [2, 3, 1, 4, 5, 7, 9, 0, 8, 6]

m = 0
n= 0
for i in l:
    if i > n:
        n = m
        m = i
print(m , n)












# Create a job table and user table


#Table User: id, name, email, mobile, resume-filefield

# Table job, Id, Title , description, location,Postedby ->FK-> UserTable, Applied-by->M2M->JOBUSerTable

#update JOBUSerTable set Applied-by=3 where job_id=1

# select u.id, u.name , u.email , j.title from user u join job j on u.id=j.postedby where u.email="aakash.sharma@gmail.com"