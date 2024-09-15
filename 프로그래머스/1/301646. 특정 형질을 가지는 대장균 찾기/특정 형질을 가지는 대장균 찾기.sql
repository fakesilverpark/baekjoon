#비트 연산자 활용하기
/*select count(*) as COUNT from ECOLI_DATA
where (((GENOTYPE & 2) = 0) and ((GENOTYPE & 1) or (GENOTYPE & 4)));*/

#와일드카드 활용하기
select count(*) as COUNT from ECOLI_DATA
where (bin(GENOTYPE) not like "%1_") and ((bin(GENOTYPE) like "%1") or (bin(GENOTYPE) like "%1__"));