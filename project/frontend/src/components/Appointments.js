import React, { useState, useEffect } from 'react';
import { api } from '../api';

function Appointments() {
  const [appointments, setAppointments] = useState([]);
  const [formData, setFormData] = useState({
    patient_name: '',
    email: '',
    date: '',
    time: '',
    reason: '',
  });

  // Fetch all appointments
  const fetchAppointments = async () => {
    try {
      const response = await api.get('/appointments');
      setAppointments(response.data);
    } catch (err) {
      console.error('Error fetching appointments:', err);
    }
  };

  // Create a new appointment
  const createAppointment = async (e) => {
    e.preventDefault();
    try {
      await api.post('/appointments', formData);
      fetchAppointments(); // Refresh the list
      setFormData({ patient_name: '', email: '', date: '', time: '', reason: '' });
    } catch (err) {
      console.error('Error creating appointment:', err);
    }
  };

  // Delete an appointment
  const deleteAppointment = async (id) => {
    try {
      await api.delete(`/appointments/${id}`);
      fetchAppointments(); // Refresh the list
    } catch (err) {
      console.error('Error deleting appointment:', err);
    }
  };

  useEffect(() => {
    fetchAppointments();
  }, []);

  return (
    <div>
      <h1>Appointments</h1>
      <form onSubmit={createAppointment}>
        <input
          type="text"
          placeholder="Patient Name"
          value={formData.patient_name}
          onChange={(e) => setFormData({ ...formData, patient_name: e.target.value })}
          required
        />
        <input
          type="email"
          placeholder="Email"
          value={formData.email}
          onChange={(e) => setFormData({ ...formData, email: e.target.value })}
          required
        />
        <input
          type="date"
          value={formData.date}
          onChange={(e) => setFormData({ ...formData, date: e.target.value })}
          required
        />
        <input
          type="time"
          value={formData.time}
          onChange={(e) => setFormData({ ...formData, time: e.target.value })}
          required
        />
        <textarea
          placeholder="Reason"
          value={formData.reason}
          onChange={(e) => setFormData({ ...formData, reason: e.target.value })}
          required
        />
        <button type="submit">Create Appointment</button>
      </form>

      <ul>
        {appointments.map((appt) => (
          <li key={appt.id}>
            <strong>{appt.patient_name}</strong> - {appt.date} at {appt.time}
            <button onClick={() => deleteAppointment(appt.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Appointments;

