textx generate --target dot --overwrite $1 -o .
textx generate --target dot --grammar $1 --overwrite $2 -o .
mv *.dot renders
dot -Tpng -O  renders/*.dot
rm -r renders/*.dot