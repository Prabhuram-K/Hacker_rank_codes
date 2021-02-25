read n

sumofodd=0
sumofeven=0

for ((i=0;i<n;i++))
do
read input
((square=$input*$input))
((temp=$input%2))

if [ $temp -eq 0 ]
then
((sumofeven=$sumofeven+$square))
else
((sumofodd=$sumofodd+$square))
fi

done

((difference=$sumofeven-$sumofodd))
echo $difference
