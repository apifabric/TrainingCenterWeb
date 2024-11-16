import { Injector, ViewChild, Component, OnInit, ViewEncapsulation } from '@angular/core';
import { OFormComponent, OntimizeService, OListPickerComponent, OTableComponent, ORealPipe, ONIFInputComponent } from 'ontimize-web-ngx';


@Component({
  selector: 'Course-detail',
  templateUrl: './Course-detail.component.html',
  styleUrls: ['./Course-detail.component.scss']
})
export class CourseDetailComponent implements OnInit  {
  protected service: OntimizeService;

  @ViewChild('oDetailForm') form: OFormComponent;
  
  constructor(protected injector: Injector) {
    this.service = this.injector.get(OntimizeService);
  }

  ngOnInit() {
    this.configureService();
  }

  protected configureService() {
    const conf = this.service.getDefaultServiceConfiguration();
    conf['path'] = '/Course';
    this.service.configureService(conf);
  }
  onDataLoaded(e: object) {
    console.log(JSON.stringify(e));
  }

}