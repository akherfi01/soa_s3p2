import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './components/Navbar';
import Appointments from './components/Appointments';
import PatientHistory from './components/PatientHistory';

function App() {
  return (
    <Router>
      <Navbar />
      <Switch>
        <Route path="/appointments" component={Appointments} />
        <Route path="/patients/:patientId/history" component={PatientHistory} />
      </Switch>
    </Router>
  );
}

export default App;

