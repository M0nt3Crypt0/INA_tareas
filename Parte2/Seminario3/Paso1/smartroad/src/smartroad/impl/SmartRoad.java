package smartroad.impl;

public class SmartRoad {
	
	protected SmartRoad_RoadIncidentsSubscriber subscriber  = null;
	protected String id = null;
	
	public SmartRoad(String id) {
		this.setId(id);
		this.subscriber = new SmartRoad_RoadIncidentsSubscriber(this);
		this.subscriber.connect();
		this.subscriber.subscribe("es/upv/pros/tatami/smartcities/traffic/PTPaterna/road/" + id + "/alerts");

	}

	 public String getId() {
		return id;
	}
	 
	 public void setId(String id) {
		this.id = id;
	}
	 
	
}
