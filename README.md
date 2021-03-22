# How to run this?

 * <Open the terminal/shell and insert>

                     https://github.com/tvhoang0450/ask_ans_api.git


 * <You can create virtual environment but its optional>

                                 pip install -r requirements.txt

                                 python3 manage.py makemigrations

                                 python3 manage.py migrate

                                 python3 manage.py runserver

 * >> <Then open browser and go to 'http://127.0.0.1:8000/' >

 *   " http://127.0.0.1:8000/ " is the root of project.

 *  Then you can navigate to 
    "http://127.0.0.1:8000/rest-auth/"
                        or 
    "http://127.0.0.1:8000/qa/"


 * >> Better if you go to "http://127.0.0.1:8000/rest-auth/registration/"
 * After register navigate " http://127.0.0.1:8000/rest-auth/login "

 * >> Then you are an Authenticated User

 * visit "http://127.0.0.1:8000/qa/"

 * Upvote/downvote Question "http://127.0.0.1:8000/qa/question/<int:qn_id>/like/" ^where <int:qn_id> is any id of the post(try giving 1,2,3,4,)
 * Upvote/downvote Answer "http://127.0.0.1:8000/qa/answer/<int:qn_id>/like/" ^where <int:qn_id> is any id of the post(try giving 1,2,3,4,)


 * Or you can run with docker: docker run -itd --name tetsv3 -p 8000:8000 tvh0711/django:v3
 * I run a example in Ip address: http://139.162.54.191:8000/
 * Supperuser (username: admin, password: admin)
