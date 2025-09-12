textx generate --target dot --overwrite $2 -o .
textx generate --target dot --grammar $2 --overwrite $3 -o .
mv *.dot renders
dot -Tpng -O  renders/*.dot
rm -r renders/*.dot