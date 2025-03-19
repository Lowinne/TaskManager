from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

firefox_path = "C:/Program Files/Mozilla Firefox/firefox.exe" 

options = Options()
options.binary_location = firefox_path  

gecko_path = 'C:/Users/boris/Documents/EFREI/Workspace/Test E2E/test_unitaire_rendu/TaskManager/geckodriver.exe'
service = Service(gecko_path)

driver = webdriver.Firefox(service=service, options=options)

def test_add_task_with_due_date():
    driver.get('file:///C:/Users/boris/Documents/EFREI/Workspace/Test E2E/test_unitaire_rendu/TaskManager/src/html/index_exercice 3.html')

    wait = WebDriverWait(driver, 10)

    # Remplir le champ de tâche et de date
    task_input = wait.until(EC.presence_of_element_located((By.ID, 'taskInput')))
    due_date_input = driver.find_element(By.ID, 'taskDueDate')
    add_button = driver.find_element(By.XPATH, "//button[text()='Ajouter']")

    task_input.send_keys("Tâche avec échéance")
    due_date_input.send_keys("2025-03-25")
    add_button.click()

    # Vérifier si la tâche a bien été ajoutée
    task_list = wait.until(EC.presence_of_element_located((By.ID, 'taskList')))
    tasks = task_list.find_elements(By.CLASS_NAME, 'task-item')

    assert len(tasks) > 0, "La tâche n'a pas été ajoutée correctement."
    assert "Tâche avec échéance - Échéance: 2025-03-25" in tasks[-1].text, "Le texte de la tâche ajoutée est incorrect."

    print("✅ Test d'ajout de tâche avec échéance réussi.")

def test_remove_task():
    driver.get('file:///C:/Users/boris/Documents/EFREI/Workspace/Test E2E/test_unitaire_rendu/TaskManager/src/html/index_exercice 3.html')

    wait = WebDriverWait(driver, 10)

    # Ajouter une tâche
    task_input = wait.until(EC.presence_of_element_located((By.ID, 'taskInput')))
    due_date_input = driver.find_element(By.ID, 'taskDueDate')
    add_button = driver.find_element(By.XPATH, "//button[text()='Ajouter']")
    
    task_input.send_keys("Tâche à supprimer")
    due_date_input.send_keys("2025-03-30")
    add_button.click()

    # Supprimer la tâche
    task_list = wait.until(EC.presence_of_element_located((By.ID, 'taskList')))
    task_item = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'task-item')))[-1]
    delete_button = task_item.find_element(By.XPATH, ".//button[text()='Supprimer']")
    
    delete_button.click()
    time.sleep(1)  # Petit délai pour la mise à jour

    # Vérifier que la tâche n'est plus présente
    tasks = task_list.find_elements(By.CLASS_NAME, 'task-item')
    assert len(tasks) == 1, "La tâche n'a pas été supprimée correctement."

    print("✅ Test de suppression de tâche réussi.")

# 🚀 Exécution des tests
try:
    test_add_task_with_due_date()
    test_remove_task()
finally:
    driver.quit()
