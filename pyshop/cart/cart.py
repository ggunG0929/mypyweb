# 장바구니 - 세션(session)
from decimal import Decimal     # _decimal에서 일단 _ 빼봄
from django.conf import settings

from shop.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session  # 세션 발급
        cart = self.session.get(settings.CART_ID)   # 장바구니 생성   # import settings - django conf
        if not cart:
            cart = self.session[settings.CART_ID] = {}  # 없으면 빈 장바구니 생성(딕셔너리 형태)
        self.cart = cart    # 세션에서 가져온 카트

    def __len__(self):  # 수량 합계
        return sum(item['quantity'] for item in self.cart.values())
    
    # 반복 메서드(함수)
    def __iter__(self):
        product_ids = self.cart.keys()     # 제품 번호들로 리스트
        # 리스트에서 해당 id의 모든 제품
        products = Product.objects.filter(id__in=product_ids)   # import Product
        
        for product in products:
            self.cart[str(product.id)]['product'] = product    # 해당 제품을 카트에 저장

        # 제품에 대한 내용 변경
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])  # 숫자형으로 변환  # import Decimal
            # 제품당 총 합계액 = 단위당 가격 * 수량
            item['total_price'] = item['price'] * item['quantity']

            yield item  # item을 반환(return)

    # 장바구니에 제품 추가
    def add(self, product, quantity=1, is_update=False):
        product_id = str(product.id)
        # 카트에 제품이 없는 경우
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        # 카트에 제품이 있는 경우
        if is_update:
            self.cart[product_id]['quantity'] = quantity    # 수량 변경
        else:
            self.cart[product_id]['quantity'] += quantity    # 수량 증가
        self.save()

    # 장바구니 저장
    def save(self):
        self.session[settings.CART_ID] = self.cart
        self.session.modified = True

    # 주문 총 금액
    def get_product_total(self):
        return sum(item['price']*item['quantity'] for item in self.cart.values())

    # 장바구니 속 제품 삭제
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del(self.cart[product_id])  # del()로 삭제
            self.save()
