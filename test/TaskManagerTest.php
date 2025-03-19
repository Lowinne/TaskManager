<?php

use PHPUnit\Framework\TestCase;
use Boris\TaskManager\model\TaskManager;

class TaskManagerTest extends TestCase 
{
    public $taskManager;
    public $task1 = "task1";
    public $task2 = "task2";

    protected function setUp(): void{
        $this->taskManager = new TaskManager();
        $this->taskManager->addTask($this->task1);
        $this->taskManager->addTask($this->task2);
    }

    public function testAddTask(): void {
        //init test
        $taskManager = new TaskManager();
        $taskManager->addTask($this->task1);
        // test de l'ajout de tache
        $this->assertEquals([$this->task1] , $taskManager->getTasks());
    }

    public function testRemoveTask(): void {        
        //Test de la suppression de tache 
        $this->taskManager->removeTask(1);

        //Assert
        $this->assertCount(1, $this->taskManager->getTasks());
        $this->assertEquals([$this->task1] , $this->taskManager->getTasks());
    }

    public function testGetTasks(): void {
        //Recupération de toutes les taches
        $this->assertEquals([$this->task1, $this->task2] , $this->taskManager->getTasks());
    }

    public function testGetTask(): void {
        //Recuperation d'une tache specifique selon son index
        $this->assertEquals( $this->task1, $this->taskManager->getTask(0));
        $this->assertEquals( $this->task2, $this->taskManager->getTask(1));
    }

    public function testRemoveInvalidIndexThrowsException(): void {
        $this->expectException(OutOfBoundsException::class);
        $this->taskManager->removeTask(2);
    }

    public function testGetInvalidIndexThrowsException(): void {
        $this->expectException(OutOfBoundsException::class);
        $this->taskManager->getTask(2);
    }

    public function testTaskOrderAfterRemoval(): void {
        $this->taskManager->addTask("task3");
        $this->taskManager->removeTask(1);
        //Test de l'ordre des taches apres suppression
        $this->assertEquals([$this->task1, "task3"] , $this->taskManager->getTasks());
    }

    protected function tearDown(): void
    {
        $this->taskManager = null;
        $this->task1 = null;
        $this->task2 = null;
    }
}

