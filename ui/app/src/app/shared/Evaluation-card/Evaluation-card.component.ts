import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Evaluation-card.component.html',
  styleUrls: ['./Evaluation-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Evaluation-card]': 'true'
  }
})

export class EvaluationCardComponent {


}