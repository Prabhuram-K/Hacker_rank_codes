read num1
read num2


for (( i=1; i<num1; i++))
do
((j = $num1 % $i))
if [ $j -eq 0 ]
then
((sum1=sum1+$i))
#echo $i
fi
done
#echo $sum1


for (( i=1; i<num2; i++))
do
((j = $num2 % $i))
if [ $j -eq 0 ]
then
((sum2=sum2+$i))
#echo $i
fi
done
#echo $sum2


if [[ ( $num1 == $sum2 && $num2 == $sum1 ) ]]
then
echo "The pair is amicable"
else
echo "The pair is not amicable"
fi
