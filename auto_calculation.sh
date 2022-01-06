#!/bin/bash
i=0
for ((med=80; med<1530; med+=50)); do
for ((dm=10; 2*dm<${med}; dm+=20)); do
python make_param_card.py ${med} ${dm} ${i}

#combine -M Significance datacard/"${med}_${dm}_no_datacard".txt -t -1 --expectSignal=1
combine -M AsymptoticLimits datacard/"${med}_${dm}_datacard".txt --run blind

(( i++ ))
done
done

