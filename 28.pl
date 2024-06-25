symptom(fever).
symptom(cough).
symptom(headache).
symptom(fatigue).
disease(cold).
disease(flu).
disease(covid19).

has_symptom(cold, cough).
has_symptom(cold, headache).
has_symptom(flu, fever).
has_symptom(flu, cough).
has_symptom(flu, headache).
has_symptom(flu, fatigue).
has_symptom(covid19, fever).
has_symptom(covid19, cough).
has_symptom(covid19, fatigue).

diagnose(Disease, Symptoms) :-
    disease(Disease),
    findall(Symptom, has_symptom(Disease, Symptom), Symptoms).
