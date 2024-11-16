import { Injector, ViewChild, Component, OnInit, ViewEncapsulation } from '@angular/core';
import { OFormComponent, OntimizeService, OListPickerComponent, OTableComponent, ORealPipe, ONIFInputComponent } from 'ontimize-web-ngx';


@Component({
  selector: 'Evaluation-detail',
  templateUrl: './Evaluation-detail.component.html',
  styleUrls: ['./Evaluation-detail.component.scss']
})
export class EvaluationDetailComponent implements OnInit  {
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
    conf['path'] = '/Evaluation';
    this.service.configureService(conf);
  }
  onDataLoaded(e: object) {
    console.log(JSON.stringify(e));
  }

}