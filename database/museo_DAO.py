from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass


    def get_musei(self):
        results = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Connection failed")
            return None

        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * FROM museo"""
            cursor.execute(query)
            for row in cursor:
                museo = Museo(row["id"], row["nome"], row["tipologia"])
                results.append(museo)
            #print(results)
            cursor.close()
            cnx.close()
            return results


    def get_epoche(self):
        results = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Connection failed")
            return None

        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT(epoca) FROM artefatto"""
            cursor.execute(query)
            for row in cursor:
                results.append(row["epoca"])
            #print(results)
            cursor.close()
            cnx.close()
            return results



    # TODO
