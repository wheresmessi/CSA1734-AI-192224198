diet(celiac,gluten_free).
diet(diabetes,low_sugar).
diet(hypertension,low_sodium).
diet(anemia,high_iron).
diet(obesity,low_calorie).

suggest_diet(Disease,Diet):- diet(Disease,Diet).
