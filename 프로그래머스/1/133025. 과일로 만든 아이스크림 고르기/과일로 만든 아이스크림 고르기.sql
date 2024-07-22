select f.FLAVOR from FIRST_HALF f, ICECREAM_INFO i
where f.FLAVOR = i.FLAVOR and INGREDIENT_TYPE = 'fruit_based' and TOTAL_ORDER > 3000
order by TOTAL_ORDER desc;