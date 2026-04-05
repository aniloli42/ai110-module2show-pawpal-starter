"""
pawpal_system.py
Logic layer for PawPal+ — pet care planning assistant.

Classes:
    Task     — a single pet care activity
    Pet      — a pet with a list of care tasks
    Owner    — a pet owner with a daily time budget
    Schedule — a generated daily care plan for one owner + pet
    PawPal   — root registry that manages all owners and schedules
"""

import uuid
from dataclasses import dataclass, field
from typing import Optional


# ---------------------------------------------------------------------------
# Task
# ---------------------------------------------------------------------------

@dataclass
class Task:
    """Represents a single pet care activity."""

    VALID_PRIORITIES = {"low", "medium", "high"}
    VALID_CATEGORIES = {"walk", "feeding", "meds", "grooming", "enrichment", "other"}

    pet_id: str
    title: str
    duration_minutes: int
    priority: str = "medium"
    category: str = "other"
    notes: str = ""
    id: str = field(default_factory=lambda: str(uuid.uuid4()), init=False)

    def is_high_priority(self) -> bool:
        """Returns True if the task priority is 'high'."""
        pass

    def to_dict(self) -> dict:
        """Serializes the task to a plain dictionary."""
        pass


# ---------------------------------------------------------------------------
# Pet
# ---------------------------------------------------------------------------

@dataclass
class Pet:
    """Represents a pet with a list of care tasks."""

    owner_id: str
    name: str
    species: str
    breed: str = ""
    age: int = 0
    tasks: list[Task] = field(default_factory=list)
    id: str = field(default_factory=lambda: str(uuid.uuid4()), init=False)

    def add_task(self, task: Task) -> None:
        """Adds a care task to this pet."""
        pass

    def remove_task(self, task_id: str) -> None:
        """Removes a task by its unique ID."""
        pass

    def get_tasks(self) -> list[Task]:
        """Returns all tasks assigned to this pet."""
        pass

    def get_task(self, task_id: str) -> Optional[Task]:
        """Returns a specific task by ID, or None if not found."""
        pass


# ---------------------------------------------------------------------------
# Owner
# ---------------------------------------------------------------------------

@dataclass
class Owner:
    """Represents a pet owner with a daily time budget and a list of pets."""

    name: str
    available_minutes: int = 120
    preferences: list[str] = field(default_factory=list)
    pets: list[Pet] = field(default_factory=list)
    id: str = field(default_factory=lambda: str(uuid.uuid4()), init=False)

    def add_pet(self, pet: Pet) -> None:
        """Adds a pet to the owner's list."""
        pass

    def remove_pet(self, pet_id: str) -> None:
        """Removes a pet by its unique ID."""
        pass

    def get_pets(self) -> list[Pet]:
        """Returns all pets owned by this owner."""
        pass

    def get_pet(self, pet_id: str) -> Optional[Pet]:
        """Returns a specific pet by ID, or None if not found."""
        pass


# ---------------------------------------------------------------------------
# Schedule
# ---------------------------------------------------------------------------

@dataclass
class Schedule:
    """Generated daily care plan for one owner + pet combination."""

    owner_id: str
    pet_id: str
    date: str
    tasks: list[Task]                                                       # input: tasks to schedule from
    id: str = field(default_factory=lambda: str(uuid.uuid4()), init=False)
    scheduled_tasks: list[Task] = field(default_factory=list, init=False)   # output: tasks that fit
    unscheduled_tasks: list[Task] = field(default_factory=list, init=False) # output: tasks that didn't fit
    total_duration_minutes: int = field(default=0, init=False)              # output: total time used

    def generate(self, available_minutes: int) -> None:
        """
        Sorts tasks by priority (high → medium → low), then fills the schedule
        up to available_minutes. Remaining tasks go to unscheduled_tasks.
        """
        pass

    def explain(self) -> str:
        """
        Returns a human-readable explanation of the schedule:
        which tasks were chosen, why, and what was skipped.
        """
        pass

    def get_task(self, task_id: str) -> Optional[Task]:
        """Returns a specific scheduled task by ID, or None if not found."""
        pass

    def to_dict(self) -> dict:
        """Serializes the full schedule to a plain dictionary."""
        pass


# ---------------------------------------------------------------------------
# PawPal  (root registry)
# ---------------------------------------------------------------------------

@dataclass
class PawPal:
    """
    Root application registry.
    Manages all owners and schedules and provides top-level lookup methods.
    """

    owners: list[Owner] = field(default_factory=list)
    schedules: list[Schedule] = field(default_factory=list)

    # --- Owner management ---

    def add_owner(self, owner: Owner) -> None:
        """Registers a new owner."""
        pass

    def remove_owner(self, owner_id: str) -> None:
        """Removes an owner by ID."""
        pass

    def get_owners(self) -> list[Owner]:
        """Returns all registered owners."""
        pass

    def get_owner(self, owner_id: str) -> Optional[Owner]:
        """Returns a specific owner by ID, or None if not found."""
        pass

    # --- Pet lookup (via owner) ---

    def get_pets(self, owner_id: str) -> list[Pet]:
        """Returns all pets belonging to a specific owner."""
        pass

    def get_pet(self, pet_id: str) -> Optional[Pet]:
        """Returns a specific pet by ID across all owners, or None if not found."""
        pass

    # --- Schedule management ---

    def add_schedule(self, schedule: Schedule) -> None:
        """Stores a generated schedule."""
        pass

    def remove_schedule(self, schedule_id: str) -> None:
        """Removes a schedule by ID."""
        pass

    def get_schedules(self, owner_id: str) -> list[Schedule]:
        """Returns all schedules belonging to a specific owner."""
        pass

    def get_schedule(self, schedule_id: str) -> Optional[Schedule]:
        """Returns a specific schedule by ID, or None if not found."""
        pass
