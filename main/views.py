from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from .models import Products,Cats,News
from .serializers import NewsSerializers,ProductsSerializers,CatsSerializers
# Create your views here.



class ListAPIProducts(APIView):
    def get(self,requets:Request):
        product=Products.objects.all()
        return Response(ProductsSerializers(product,many=True).data)

    def post(self,request:Request):
        serializer=ProductsSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        product=serializer.save()
        return Response(ProductsSerializers(product).data)


    def put(self,request:Request,pk=None):
        product=Products.objects.get(pk=pk)
        serializer=ProductsSerializers(instance=product,data=request.data)
        serializer.is_valid(raise_exception=True)
        product=serializer.save()
        return Response(ProductsSerializers(product).data)








class ListAPICats(APIView):
    def get(self, requets):
        cat = Cats.objects.all()
        return Response(CatsSerializers(cat, many=True).data)

    def post(self, request: Request):
        serializer = CatsSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        cat = serializer.save()
        return Response(CatsSerializers(cat).data)


    def put(self,request:Request,pk=None):
        cat=Cats.objects.get(pk=pk)
        serializer=CatsSerializers(instance=cat,data=request.data)
        serializer.is_valid(raise_exception=True)
        cat=serializer.save()
        return Response(CatsSerializers(cat).data)



class ListAPINews(APIView):
    def get(self, requets):
        news = News.objects.all()
        return Response(CatsSerializers(news, many=True).data)

    def post(self, request: Request):
        serializer = NewsSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        news = serializer.save()
        return Response(NewsSerializers(news).data)

    def put(self,request:Request,pk=None):
        news=News.objects.get(pk=pk)
        serializer=NewsSerializers(instance=news,data=request.data)
        serializer.is_valid(raise_exception=True)
        news=serializer.save()
        return Response(NewsSerializers(news).data)


