import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import Appointments from './components/Appointments';
import PatientHistory from './components/PatientHistory';

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/appointments" element={<Appointments />} />
        <Route path="/patients/:patientId/history" element={<PatientHistory />} />
      </Routes>
    </Router>
  );
}

export default App;

