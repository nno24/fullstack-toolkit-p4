var today = new Date();

// Initialize date and time pickers materialize

const Calendar = document.querySelector('.datepicker');
M.Datepicker.init(Calendar,{
    format: 'yyyy-mm-dd',
    minDate: new Date(today.getFullYear(),today.getMonth(),today.getDate()),
})

const Time = document.querySelector('.timepicker');
M.Timepicker.init(Time,{
    twelveHour:false
})

// Initialize mobile menu

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {
      'edge': 'right',
    });
  });


  // Initilalize modals

  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, {});
  });


//Initialize dropdown
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.dropdown-trigger');
    var instances = M.Dropdown.init(elems, {
      'coverTrigger': false,
      'inDuration': 500,
      'outDuration': 300,
    });
  });