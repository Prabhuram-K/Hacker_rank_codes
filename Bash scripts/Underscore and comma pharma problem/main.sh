grep -i "tb" inputfile | awk -F",|_" '
BEGIN{a=0}
{
  if($3 > 10)
  {
   print $1"_"$2"_"$3
  }
  else a=a+1
}
END { if(a==NR) print "No medicines found with greater than 10 numbers in a strip"} '
