from django.shortcuts import render
from django.http import HttpResponse
from django_src_app.mysql_model import lprod_model

# Create your views here.
def index(request):
    # return render(request,'django_src_app/index.html',{})

    # return render(request, 
    #     'django_src_app/index.html',
    #     {
    #         "msg" : '3. 잘 나옵니다'
    #     })

    # return render(request, 
    #     'django_src_app/index.html',
    #     {
    #         "msg" : '3. 잘 나옵니다',
    #         'msg_list' : ['4. 리스트 전달 잘 됩니다','4. 리스트 전달 정말 잘 됩니다']
    #     })

    # return render(request, 
    #     'django_src_app/index.html',
    #     {
    #         "msg" : '3. 잘 나옵니다',
    #         'msg_list' : [['4. 리스트 전달 잘 됩니다','4. 리스트 전달 정말 잘 됩니다'],['5. 잘나옴','5. 정말 잘 나옴']],
    #     })

    # return render(request, 
    #     'django_src_app/index.html',
    #     {
    #         "msg" : '3. 잘 나옵니다',
    #         'msg_list' : [['4. 리스트 전달 잘 됩니다','4. 리스트 전달 정말 잘 됩니다'],['5. 잘나옴','5. 정말 잘 나옴']],
    #         "msg_dic" : {
    #             'id': '6. 잘~ 나옵니다',
    #             'name' : '딕셔너리 잘~ 나옵니다'
    #         },
    #     })
        
    return render(request, 
        'django_src_app/index.html',
        {
            "msg" : '3. 잘 나옵니다',
            'msg_list' : [['4. 리스트 전달 잘 됩니다','4. 리스트 전달 정말 잘 됩니다'],['5. 잘나옴','5. 정말 잘 나옴']],
            "msg_dic" : [
                {'id': '7. 잘~ 나옵니다',
                'name' : '딕셔너리 잘~ 나옵니다'},
                {'id': '7.1 잘~ 나옵니다',
                'name' : '딕셔너리 잘~ 나옵니다'}
            ],
        })

def lprodList(request):
    list_rows = lprod_model.getLprodList()
    data = {"list_rows" : list_rows}
    return render(request,"django_src_app/lprod/lprodList.html",data)

### image, css, javascript 파일 등이 이곳에 위치하면됨..
def viewStaticImg(request) :
    return render(request, 
                    "django_src_app/imgView/viewStaticImg.html", 
                    {})