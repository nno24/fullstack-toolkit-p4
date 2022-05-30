// Initialize date and time pickers materialize

const Calendar = document.querySelector('.datepicker');
M.Datepicker.init(Calendar,{
    format: 'yyyy-mm-dd'
})

const Time = document.querySelector('.timepicker');
M.Timepicker.init(Time,{
    twelveHour:false
})

// Initialize mobile menu

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {});
  });


  // Initilalize modals

  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, {});
  });
