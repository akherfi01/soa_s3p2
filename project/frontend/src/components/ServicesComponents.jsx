import React, { useState } from 'react';
import axios from 'axios';

// Fetch Patient History
const PatientHistory = () => {
    const [patientId, setPatientId] = useState('');
    const [history, setHistory] = useState(null);
    const [error, setError] = useState(null);

    const fetchHistory = async () => {
        try {
            const response = await axios.get(`/patients/${patientId}/history`);
            setHistory(response.data);
            setError(null);
        } catch (err) {
            setError(err.response?.data?.error || 'An error occurred');
        }
    };

    return (
        <div>
            <h3>Patient History</h3>
            <input
                type="number"
                placeholder="Enter Patient ID"
                value={patientId}
                onChange={(e) => setPatientId(e.target.value)}
            />
            <button onClick={fetchHistory}>Fetch History</button>
            {history && <pre>{JSON.stringify(history, null, 2)}</pre>}
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    );
};

// Create Appointment
const CreateAppointment = () => {
    const [formData, setFormData] = useState({ patient_name: '', email: '', date: '' });
    const [response, setResponse] = useState(null);

    const createAppointment = async () => {
        try {
            const response = await axios.post('/appointments', formData);
            setResponse(response.data);
        } catch (err) {
            console.error(err);
        }
    };

    return (
        <div>
            <h3>Create Appointment</h3>
            <input
                type="text"
                placeholder="Patient Name"
                value={formData.patient_name}
                onChange={(e) => setFormData({ ...formData, patient_name: e.target.value })}
            />
            <input
                type="email"
                placeholder="Email"
                value={formData.email}
                onChange={(e) => setFormData({ ...formData, email: e.target.value })}
            />
            <input
                type="date"
                value={formData.date}
                onChange={(e) => setFormData({ ...formData, date: e.target.value })}
            />
            <button onClick={createAppointment}>Create Appointment</button>
            {response && <p>Appointment created successfully!</p>}
        </div>
    );
};

// Send Notification
const SendNotification = () => {
    const [notification, setNotification] = useState({ recipient: '', subject: '', message: '' });
    const [response, setResponse] = useState(null);

    const sendNotification = async () => {
        try {
            const response = await axios.post('/notifications', notification);
            setResponse(response.data);
        } catch (err) {
            console.error(err);
        }
    };

    return (
        <div>
            <h3>Send Notification</h3>
            <input
                type="email"
                placeholder="Recipient Email"
                value={notification.recipient}
                onChange={(e) => setNotification({ ...notification, recipient: e.target.value })}
            />
            <input
                type="text"
                placeholder="Subject"
                value={notification.subject}
                onChange={(e) => setNotification({ ...notification, subject: e.target.value })}
            />
            <textarea
                placeholder="Message"
                value={notification.message}
                onChange={(e) => setNotification({ ...notification, message: e.target.value })}
            ></textarea>
            <button onClick={sendNotification}>Send Notification</button>
            {response && <p>Notification sent successfully!</p>}
        </div>
    );
};

export { PatientHistory, CreateAppointment, SendNotification };
