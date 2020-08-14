# machineLearning-reseauElectrique
Dans le domaine des réseaux électriques, le critère de sécurité est défini par une exploitation des lignes dans leurs limites opérationnelles. Traditionnellement, les gestionnaires de réseau de transport (GRT) utilisent les calculs de « load flow » afin de déterminer les flux de puissance des lignes. La première étape, a été le développement d’un algorithme de load flow basé sur la méthode itérative de Newton-Raphson.  Après validation, cet algorithme a permis de générer les jeux de données nécessaires à l’entraînement et l’évaluation des modèles de machine learning. Ces derniers ont pour but de classifier les situations en deux catégories : saine ou à risque. Les performances sont examinées selon les deux types d’erreurs possibles : les non-détections et les fausses alarmes. Selon ces critères, deux modèles se distinguent, le réseau de neurones et l’estimateur à vecteur de support.
