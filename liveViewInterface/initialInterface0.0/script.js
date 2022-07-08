// Room Class
class Room {
  constructor(AndrewID, RoomType, TimeSlot, RoomCapacity, EnergyUse) {
    this.AndrewID = AndrewID;
    this.RoomType = RoomType;
    this.TimeSlot = TimeSlot;
    this.RoomCapacity = RoomCapacity;
    this.EnergyUse = EnergyUse;
    
  }
}

// UI Class: Handle UI Tasks
class UI {
  static displayRooms() {
    const rooms = Store.getRooms();

    rooms.forEach((room) => UI.addRoomToList(room));
  }

  static addRoomToList(room) {
    const list = document.querySelector('#room_reservation');

    const row = document.createElement('tr');

    row.innerHTML = `
      <td>${room.AndrewID}</td>
      <td>${room.RoomType}</td>
      <td>${room.TimeSlot}</td>
      <td>${room.RoomCapacity}</td>
      <td>${room.EnergyUse}</td>
      <td><a href="#" class="btn btn-warning btn-sm delete">X</a></td>
    `;

    list.appendChild(row);
  }

  static deleteRoom(el) {
    if(el.classList.contains('delete')) {
      el.parentElement.parentElement.remove();
    }
  }

  static showAlert(message, className) {
    const div = document.createElement('div');
    div.className = `alert alert-${className}`;
    div.appendChild(document.createTextNode(message));
    const container = document.querySelector('.container');
    const form = document.querySelector('#room-form');
    container.insertBefore(div, form);

    // Vanish in 3 seconds
    setTimeout(() => document.querySelector('.alert').remove(), 3000);
  }

  static clearFields() {
    document.querySelector('#AndrewID').value = '';
    document.querySelector('#RoomType').value = '';
    document.querySelector('#TimeSlot').value = '';
    document.querySelector('#RoomCapacity').value = '';
    document.querySelector('#EnergyUse').value = '';
  }
}

// Store Class: Handles Storage
class Store {
  static getRooms() {
    let rooms;
    if(localStorage.getItem('rooms') === null) {
      rooms = [];
    } else {
      rooms = JSON.parse(localStorage.getItem('rooms'));
    }

    return rooms;
  }

  static addRoom(room) {
    const rooms = Store.getRooms();
    rooms.push(room);
    localStorage.setItem('rooms', JSON.stringify(rooms));
  }

  static removeroom(AndrewID) {
    const rooms = Store.getRooms();

    rooms.forEach((room, index) => {
      if(room.AndrewID === AndrewID) {
        rooms.splice(index, 1);
      }
    });

    localStorage.setItem('rooms', JSON.stringify(rooms));
  }
}

// Event: Display Rooms
document.addEventListener('DOMContentLoaded', UI.displayRooms);

// Event: Add a Room
document.querySelector('#room-form').addEventListener('submit', (e) => {
  // Prevent actual submit
  e.preventDefault();

  // Get form values
  const AndrewID = document.querySelector('#AndrewID').value;
  const RoomType = document.querySelector('#RoomType').value;
  const TimeSlot = document.querySelector('#TimeSlot').value;
  const RoomCapacity = document.querySelector('#RoomCapacity').value;
  const EnergyUse = document.querySelector('#EnergyUse').value;

  // Validate
  if(RoomType === '' || TimeSlot === '' || AndrewID === '') {
    UI.showAlert('Please fill in all fields', 'danger');
  } else {
    // Instatiate room
    const room = new Room(AndrewID, RoomType, TimeSlot, RoomCapacity, EnergyUse);

    // Add Room to UI
    UI.addRoomToList(room);

    // Add room to store
    Store.addRoom(room);

    // Show success message
    UI.showAlert('Room Reservation Added', 'success');

    // Clear fields
    UI.clearFields();
  }
});

// Event: Remove a Room
document.querySelector('#room_reservation').addEventListener('click', (e) => {
  // Remove room from UI
  UI.deleteRoom(e.target);

  // Remove room from store
  Store.removeRoom(e.target.parentElement.previousElementSibling.textContent);

  // Show success message
  UI.showAlert('Room Reservation Removed', 'success');
});