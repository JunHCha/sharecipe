from recipe.models import Ingredient, Method, Theme


def process():
    Ingredient.objects.bulk_create(
        [
            Ingredient(name="carrot"),
            Ingredient(name="onion"),
            Ingredient(name="potato"),
            Ingredient(name="tomato"),
            Ingredient(name="brocoli"),
            Ingredient(name="mushroom"),
            Ingredient(name="garlic"),
            Ingredient(name="leek"),
            Ingredient(name="cabbage"),
            Ingredient(name="bean"),
            Ingredient(name="kimchi"),
            Ingredient(name="egg"),
            Ingredient(name="beef"),
            Ingredient(name="chicken"),
            Ingredient(name="pork"),
            Ingredient(name="fish"),
            Ingredient(name="sausage"),
            Ingredient(name="salt"),
            Ingredient(name="sugar"),
            Ingredient(name="vinegar"),
            Ingredient(name="soy sauce"),
            Ingredient(name="oil"),
            Ingredient(name="pepper"),
            Ingredient(name="noodle"),
            Ingredient(name="rice"),
            Ingredient(name="bread"),
            Ingredient(name="flour"),
            Ingredient(name="water"),
            Ingredient(name="milk"),
            Ingredient(name="cheese"),
        ]
    )
    Method.objects.bulk_create(
        [
            Method(name="boil"),
            Method(name="roast"),
            Method(name="steam"),
            Method(name="fry"),
            Method(name="bake"),
            Method(name="dry"),
            Method(name="torch"),
            Method(name="freeze"),
        ]
    )
    Theme.objects.bulk_create(
        [
            Theme(name="party"),
            Theme(name="meal"),
            Theme(name="entertainment"),
            Theme(name="nurse"),
            Theme(name="snack"),
            Theme(name="supper"),
            Theme(name="exercise"),
            Theme(name="diet"),
        ]
    )
