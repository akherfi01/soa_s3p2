import { useState } from 'react'
import './App.css'
// import { PatientHistory, CreateAppointment, SendNotification } from './components/ServicesComponents';
import CreateAppointment from "./components/CreateAppointment";

function App() {

  return (
      <div className="App">
          <h1>Welcome to the Clinic Portal</h1>
            <CreateAppointment />
     </div>
  )
}

export default App
