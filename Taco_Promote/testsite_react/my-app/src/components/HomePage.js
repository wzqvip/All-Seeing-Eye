import React from 'react';
import { Tab, Nav, Col, Row } from 'react-bootstrap';

const HomePage = () => (
  <Tab.Container id="left-tabs" defaultActiveKey="record">
    <Row>
      <Col sm={3}>
        <Nav variant="pills" className="flex-column">
          <Nav.Item>
            <Nav.Link eventKey="record">Record</Nav.Link>
          </Nav.Item>
          <Nav.Item>
            <Nav.Link eventKey="predict">Predict</Nav.Link>
          </Nav.Item>
          <Nav.Item>
            <Nav.Link eventKey="goal">Goal</Nav.Link>
          </Nav.Item>
        </Nav>
      </Col>
      <Col sm={9}>
        <Tab.Content>
          <Tab.Pane eventKey="record">
            <h1>Record</h1>
          </Tab.Pane>
          <Tab.Pane eventKey="predict">
            <h1>Predict</h1>
          </Tab.Pane>
          <Tab.Pane eventKey="goal">
            <h1>Goal</h1>
          </Tab.Pane>
        </Tab.Content>
      </Col>
    </Row>
  </Tab.Container>
);

export default HomePage;
