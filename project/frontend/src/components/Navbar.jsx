import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav>
      <ul>
        <li>
          <Link to="/appointments">Appointments</Link>
        </li>
        <li>
          <Link to="/patients/1/history">Patient History</Link>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;

