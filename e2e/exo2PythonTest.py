from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import shutil

firefox_path = "C:/Program Files/Mozilla Firefox/firefox.exe" 

options = Options()
options.binary_location = firefox_path  

gecko_path = 'C:/Users/boris/Documents/EFREI/Workspace/Test E2E/test_unitaire_rendu/TaskManager/geckodriver.exe'
service = Service(gecko_path)

driver = webdriver.Firefox(service=service, options=options)

file_path = 'file:///C:/Users/boris/Documents/EFREI/Workspace/Test E2E/test_unitaire_rendu/TaskManager/src/html/index.html'


def test_add_task():
    try:
        driver.get(file_path)
        wait = WebDriverWait(driver, 10)

        # Attendre les éléments
        task_input = wait.until(EC.presence_of_element_located((By.ID, 'taskInput')))
        add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Ajouter']")))

        # Ajouter une tâche
        task_input.send_keys("Nouvelle tâche")
        add_button.click()

        # Vérifier si la tâche apparaît
        task_list = wait.until(EC.presence_of_element_located((By.ID, 'taskList')))
        tasks = task_list.find_elements(By.CLASS_NAME, 'task-item')

        assert len(tasks) > 0, "La tâche n'a pas été ajoutée correctement."
        assert "Nouvelle tâche" in tasks[-1].text, "Le texte de la tâche est incorrect."

        print("✅ Test d'ajout de tâche réussi.")
    
    except Exception as e:
        print(f"❌ Erreur dans test_add_task: {e}")

def test_remove_task():
    try:
        driver.get(file_path)
        wait = WebDriverWait(driver, 10)

        # Ajouter une tâche à supprimer
        task_input = wait.until(EC.presence_of_element_located((By.ID, 'taskInput')))
        add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Ajouter']")))
        task_input.send_keys("Tâche à supprimer")
        add_button.click()

        # Attendre que la tâche apparaisse
        task_list = wait.until(EC.presence_of_element_located((By.ID, 'taskList')))
        tasks = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'task-item')))

        if not tasks:
            raise Exception("Aucune tâche trouvée après l'ajout.")

        # Récupérer la dernière tâche et son bouton de suppression
        task_item = tasks[-1]
        delete_button = wait.until(EC.element_to_be_clickable(task_item.find_element(By.XPATH, ".//button[text()='Supprimer']")))

        # Supprimer la tâche
        delete_button.click()

        # Vérifier que la tâche a bien disparu
        time.sleep(1)  # Petite pause pour la mise à jour de la liste
        remaining_tasks = task_list.find_elements(By.CLASS_NAME, 'task-item')
        assert len(remaining_tasks) == 0, "La tâche n'a pas été supprimée correctement."

        print("✅ Test de suppression de tâche réussi.")

    except Exception as e:
        print(f"❌ Erreur dans test_remove_task: {e}")

try:
    test_add_task()
    test_remove_task()
finally:
    driver.quit()
