import SacAdosNaif as sa
import unittest
import sys 
sys.path.append("--")
class TestMonProgramme(unittest.TestCase):


	

    

	liste_objet=[{'masse': "1", 'nom': 'A', 'valeur': "1"},{'masse': "1", 'nom': 'A', 'valeur': "10"}]
	
	def test_dic(self):

		liste_objets=sa.Ajout_Ratio(sa.liste_objets)
		taille=len(liste_objets)
		for i in range (taille):
			r=liste_objets[i].get("masse")
			x=eval(r)
			self.assertGreater(x,0,'La masse doit etre positive ou supérieur à zero')



if __name__ == "__main__":

	unittest.main()
