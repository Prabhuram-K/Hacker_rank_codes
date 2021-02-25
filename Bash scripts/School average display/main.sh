awk '
BEGIN {FS="|";OFS="|"}
(NR > 1){
  if($4 == "Sangamithra" && $5 >= 90 && $6 >= 9)
  { print $1,$2,$3,$4,($5+$6)/2 }
  }' studentsData
