import { useState } from 'react'
import './App.css'
import { PatientHistory, CreateAppointment, SendNotification } from './components/ServicesComponents';

function App() {

  return (
      <div className="App">
          <h1>Welcome to the Clinic Portal</h1>
          <PatientHistory />
          <CreateAppointment />
          <SendNotification />
     </div>
  )
}

export default App
