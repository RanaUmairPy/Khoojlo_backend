# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, ProductImage
from .Serializers import ProductSerializer

class ProductAPIView(APIView):

    # CREATE
    def post(self, request):
        name = request.data.get('name')
        description = request.data.get('description')
        price = request.data.get('price')
        images = request.FILES.getlist('images')
        category = request.data.get('category')

        product = Product.objects.create(
            name=name,
            description=description,
            price=price,
            category=category
        )

        for img in images:
            ProductImage.objects.create(product=product, images=img)

        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # READ ALL
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductDetailAPIView(APIView):

    # Helper method
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return None

    # READ SINGLE
    def get(self, request, pk):
        product = self.get_object(pk)
        if not product:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # UPDATE
    def put(self, request, pk):
        product = self.get_object(pk)
        if not product:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        product.name = request.data.get('name', product.name)
        product.description = request.data.get('description', product.description)
        product.price = request.data.get('price', product.price)
        product.save()

        # Add new images if provided
        images = request.FILES.getlist('images')
        for img in images:
            ProductImage.objects.create(product=product, image=img)

        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # DELETE
    def delete(self, request, pk):
        product = self.get_object(pk)
        if not product:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



class LatestProductsAPIView(APIView):
    def get(self, request):
        latest_products = Product.objects.order_by('-created_at')
        serializer = ProductSerializer(latest_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class Show_all(APIView):
    def get(self, request):
        all_products = Product.objects.filter().order_by('?')
        serializer = ProductSerializer(all_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class Show_Category(APIView):
    def get(self, request, category):
        category_products = Product.objects.filter(category__iexact=category).order_by('-created_at')

        serializer = ProductSerializer(category_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class product_details(APIView):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)


