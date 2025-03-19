<?php

namespace Boris\TaskManager\model;


class TaskManager
{
    private $tasks = [];

    public function __construct()
    {
        $this->tasks = [];
    }

    /**
     * Ajoute une tâche au gestionnaire
     */
    public function addTask(string $task): void
    {
        $this->tasks[] = $task;
    }

    /**
     * Supprime une tâche par son index
     * @throws OutOfBoundsException
     */
    public function removeTask(int $index): void
    {
        if (!isset($this->tasks[$index])) {
            throw new \OutOfBoundsException("Index de tâche invalide: $index");
        }

        unset($this->tasks[$index]);
        $this->tasks = array_values($this->tasks); // Réindexe le tableau
    }

    /**
     * Récupère toutes les tâches
     */
    public function getTasks(): array
    {
        return $this->tasks;
    }

    /**
     * Récupère une tâche spécifique
     * @throws OutOfBoundsException
     */
    public function getTask(int $index): string
    {
        if (!isset($this->tasks[$index])) {
            throw new \OutOfBoundsException("Index de tâche invalide: $index");
        }

        return $this->tasks[$index];
    }
}