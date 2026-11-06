"""
Citizen Complaint Management System
Course: PROG211 - Object-Oriented Programming 1

Domain: Government
DPG principles: Open-source, accessible, privacy-respecting,
modular, and reusable.
"""


class Citizen:
    """Represents an anonymous citizen using a reference ID."""

    def _init_(self, citizen_id, location):
        self.citizen_id = citizen_id
        self.location = location

    def display_info(self):
        """Display basic citizen information."""
        print(f"Citizen Reference: {self.citizen_id}")
        print(f"Location: {self.location}")


class Complaint:
    """Represents a complaint submitted to a government office."""

    total_complaints = 0

    def _init_(self, complaint_id, citizen_id, category, description):
        self.complaint_id = complaint_id
        self.citizen_id = citizen_id
        self.category = category
        self.description = description
        self.status = "Pending"
        Complaint.total_complaints += 1

    def update_status(self, new_status):
        """Update the status of a complaint."""
        allowed_statuses = ["Pending", "In Progress", "Resolved"]

        if new_status in allowed_statuses:
            self.status = new_status
            print("Complaint status updated successfully.")
        else:
            print("Invalid status. Choose Pending, In Progress, or Resolved.")

    def display_info(self):
        """Display complaint details."""
        print("-" * 45)
        print(f"Complaint ID: {self.complaint_id}")
        print(f"Citizen Reference: {self.citizen_id}")
        print(f"Category: {self.category}")
        print(f"Description: {self.description}")
        print(f"Status: {self.status}")

    @classmethod
    def get_total_complaints(cls):
        """Return the total number of complaint objects created."""
        return cls.total_complaints


class GovernmentComplaintSystem:
    """Manages citizen records and government complaints."""

    def _init_(self):
        # One data structure: a list of complaint objects
        self.complaints = []

    def add_complaint(self, complaint):
        """Add a complaint to the system."""
        for existing in self.complaints:
            if existing.complaint_id == complaint.complaint_id:
                print("Error: Complaint ID already exists.")
                return

        self.complaints.append(complaint)
        print("Complaint added successfully.")

    def display_complaints(self):
        """Display all complaints stored in the list."""
        if not self.complaints:
            print("No complaints have been recorded.")
            return

        for complaint in self.complaints:
            complaint.display_info()

    def search_complaint(self, complaint_id):
        """Find a complaint by its ID."""
        for complaint in self.complaints:
            if complaint.complaint_id == complaint_id:
                complaint.display_info()
                return complaint

        print("Complaint not found.")
        return None


def main():
    """Run the government complaint management program."""
    system = GovernmentComplaintSystem()

    # Create citizen objects using anonymous reference IDs
    citizen1 = Citizen("C001", "Freetown")
    citizen2 = Citizen("C002", "Bo")

    # Demonstrate citizen object interaction
    print("CITIZEN INFORMATION")
    citizen1.display_info()
    print()

    # Create complaint objects
    complaint1 = Complaint(
        "G001",
        citizen1.citizen_id,
        "Road Maintenance",
        "A road in the community needs repair."
    )

    complaint2 = Complaint(
        "G002",
        citizen2.citizen_id,
        "Water Supply",
        "The community has an irregular water supply."
    )

    complaint3 = Complaint(
        "G003",
        citizen1.citizen_id,
        "Waste Management",
        "Waste collection is delayed in the area."
    )

    # Add complaints to the system
    system.add_complaint(complaint1)
    system.add_complaint(complaint2)
    system.add_complaint(complaint3)

    # Display all complaints
    print("\nALL GOVERNMENT COMPLAINTS")
    system.display_complaints()

    # Update one complaint
    print("\nUPDATING COMPLAINT G001")
    complaint1.update_status("In Progress")

    # Search for a complaint
    print("\nSEARCH RESULT")
    system.search_complaint("G001")

    # Demonstrate a class method
    print("\nTOTAL COMPLAINTS CREATED:",
          Complaint.get_total_complaints())


if _name_ == "_main_":
    main(